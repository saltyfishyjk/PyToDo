class Task():
    def __init__(self,
                 text,
                 title,
                 author,
                 creatTime,
                 description) -> None:
        self.id = None
        self.text = text
        self.title = title
        self.author = author
        self.creatTime = creatTime
        self.description = description
