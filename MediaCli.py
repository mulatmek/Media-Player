import click


@click.group()
def MediaCli():
    pass


@click.command()
@click.option('--name', '-n', help="Name of the user", required=True, prompt="Enter Your Name please")
def start(name):
    print(f"hello,{name}" + " " + "from media paler")


@click.command()
@click.option('--path', '-n', help="enter a path ", required=True)
def load(path):
    print(f"your songs uploaded  {path}")


@click.command()
@click.option('--song', help="enter song", required=True)
def play(song):
    print(f"your song  {song}")


MediaCli.add_command(start)
MediaCli.add_command(load)
MediaCli.add_command(play)
