from subprocess import check_output

class Speaker:
    def __init__(self):
        print("speaker setup")

    @staticmethod
    def getSound():
        print("speaker running")
        check_output('omxplayer -o local Code/Backend/sound/sound_food.mp3', shell=True)

speaker = Speaker()
speaker.getSound()