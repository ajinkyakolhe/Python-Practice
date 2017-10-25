#Tip: dot notation tells Python to look inside the space that is before the dot for code to execute.

def pafy():
    '''
    Function that imports pafy library and connects youtube URL to view the metadata for multiple files
    :return: Some metadata which is part of video content.
    :rtype: String and int
    '''
    import pafy
    hello = ["kJQP7kiw5Fk", "JGwWNGJdvx8"]
    for i in hello:
        url = "https://www.youtube.com/watch?v=" + i
        video = pafy.new(url)
        print(video.title)
        print(video.rating)
        print(video.published + '\n')

def main():
    pafy()
if __name__ == '__main__':
    main()
