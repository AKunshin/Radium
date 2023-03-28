from git.repo import Repo


def clone_repo(url):
    Repo.clone_from(url, to_path="./downloads_3/")


def main():
    url = 'https://gitea.radium.group/radium/project-configuration'
    clone_repo(url)


if __name__ == "__main__":
    main()
