#Tip: dot notation tells Python to look inside the space that is before the dot for code to execute.

def pafy():
    '''
    Function that imports pafy library and connects youtube URL
    :return: Some metadata which is part of video content.
    :rtype: String and int
    '''
    import pafy
    url = "https://www.youtube.com/watch?v=kJQP7kiw5Fk"
    video = pafy.new(url)

    print(video.title)
    print(video.rating)
    print(video.published)

def main():
    pafy()
if __name__ == '__main__':
    main()
