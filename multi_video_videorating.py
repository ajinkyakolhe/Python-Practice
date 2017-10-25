#Tip: dot notation tells Python to look inside the space that is before the dot for code to execute.

def pafy():
    '''
    Function that imports pafy library and connects youtube URL to view the metadata for multiple files
    :return: Some metadata which is part of video content.
    :rtype: String and int
    '''
    import pafy
    hello = ["kJQP7kiw5Fk", "JGwWNGJdvx8", "G_JtNhTzg5s", "XKu_SEDAykw", "DSGsa0pu8-k", "5m0L0k8ZtEs"]
    for i in hello:
        url = "https://www.youtube.com/watch?v=" + i
        video = pafy.new(url)
        print('\n' + video.title)
        print("Likes: " + str(video.likes))
        print("Dislikes: " + str(video.dislikes))
        print(video.likes*5/(video.dislikes+video.likes))
        print(video.rating)


def main():
    pafy()
if __name__ == '__main__':
    main()
