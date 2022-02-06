from docker import from_env, errors
from os import listdir
from shutil import copyfile
import requests


ROOT_PATH = ""
CODE_PATH = ""
INPUT = ""
OUTPUT = ""
SRC_DOCKERFILES = ""


def copyDockerFiles(work_path):
    file_name = listdir(work_path)
    if "main.py" in file_name:
        copyfile(SRC_DOCKERFILES + '/python', work_path)
    elif "main.cpp" in file_name:
        copyfile(SRC_DOCKERFILES + '/cpp', work_path)
    elif "main.java" in file_name:
        copyfile(SRC_DOCKERFILES + '/java', work_path)
    else:
        # fohshhhhh bede be ganji XD
        return False
    return True


def createIMAGE(team_id, client):

    work_path = ROOT_PATH + CODE_PATH + team_id + INPUT
    if not copyDockerFiles(work_path):
        return "FILE main doesnt exist!!"

    cmp_err_msg = ""  # compile error message

    try:
        # docker build command
        client.images.build(path=work_path,
                            tag=team_id)

    except errors.BuildError as e:
        for line in e.build_log:
            if 'stream' in line:
                if not("--->" in line['stream'].strip() or "Step" in line['stream'].strip()):
                    cmp_err_msg += (line['stream'].strip())

        return cmp_err_msg.strip()
    return "ok"


def dockerRunContainer(team_id):
    client = from_env()
    res = createIMAGE(team_id, client)
    if not res == "ok":
        return res

    volume = {
        ROOT_PATH + CODE_PATH + team_id + OUTPUT: {
            'bind': '/tmp',
            'mode': 'rw',
        },
    }
    # docker run command
    # , stdin_open=True, tty=True => such -it in docker run :))
    c = client.containers.run(image=team_id, remove=True,
                              volumes=volume, detach=True)

    if not c:
        # TODO: logger benevis moein berize to discord :)
        return "container doesnt run successfully :/"
    return "ok"


def execute(team_id, api_address):
    res = dockerRunContainer(team_id)
    if not res == "ok":
        r = requests.post(api_address+"/compile-result",
                          data={'_id': team_id, 'compile_status': 'Error', 'compile_message': res})
    else:
        r = requests.post(api_address+"/compile-result",
                          data={'_id': team_id, 'compile_status': 'Success', 'compile_message': ""})


def startmatch(match_id, team1_file_name, team1_name, team2_file_name, team2_name, client):

    #TODO: envs
    env = {"team1_name": team1_name, "team1_name": team2_name}

    volume = {
        os.path.join(): {  # ROOT_PATH + /codes + team1_file_name(from ganji) + output
            'bind': '/tmp/p1',
            'mode': 'rw',
        },
        os.path.join(): {  # ROOT_PATH + /codes + team2_file_name(from ganji) + output
            'bind': '/tmp/p2',
            'mode': 'rw',
        },
        os.path.join(): {  # kernel exefile path
            'bind': '/tmp/kernel',
            'mode': 'rw',
        },
        os.path.join(): {  # ROOT_PATH + /games + match_id(from ganji)
            'bind': '/tmp/output',
            'mode': 'rw',
        },
    }

    c = client.containers.run(image="aicupjava", remove=True,
                              volumes=volume, environment=env, detach=True)

    if c:
        r = requests.post(settings.MICRO_URL + "/match-result",
                          date={'match_id': match_id, 'winner': open("kernel winner absolute path (~.~)", "r").read()})

        if not r.status_code == 200:
            logger.error("response of Micro is {}".format(str(r.json())))


def main():
    team_id = ""
    api_address = ""

    execute(team_id)


if __name__ == "__main__":
    main()
