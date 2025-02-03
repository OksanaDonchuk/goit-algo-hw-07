from typing import List


class Comments:
    def __init__(self, text: str, author: str) -> None:
        """
        Клас для представлення коментарів.

        Args:
            text (str): Текст коментаря.
            author (str): Автор коментаря.
        """
        self.text: str = text
        self.author: str = author
        self.replies: List["Comments"] = []
        self.is_deleted: bool = False

    def add_reply(self, reply: "Comments") -> None:
        """
        Додає відповідь до коментаря.

        Args:
            reply (Comments): Коментар-відповідь, який додається до replies.
        """
        self.replies.append(reply)

    def remove_reply(self) -> None:
        """
        Позначає коментар як видалений, змінюючи текст на стандартне повідомлення.
        """
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, indent: int = 0) -> None:
        """
        Виводить коментар та всі його відповіді, використовуючи відступи.

        Args:
            indent (int): Відступ для відображення ієрархії.
        """
        if self.is_deleted:
            print(" " * indent + "Цей коментар було видалено.")
        else:
            print(" " * indent + f"{self.author}: {self.text}")

        for reply in self.replies:
            reply.display(indent + 4)


# Приклад використання:
root_Comments = Comments("Яка чудова книга!", "Бодя")
reply1 = Comments("Книга повне розчарування :(", "Андрій")
reply2 = Comments("Що в ній чудового?", "Марина")

# Додаємо відповіді на кореневий коментар
root_Comments.add_reply(reply1)
root_Comments.add_reply(reply2)

# Додаємо відповідь до першого коментаря-відповіді
reply1_1 = Comments("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Видаляємо перший коментар-відповідь
reply1.remove_reply()

# Виводимо всі коментарі
root_Comments.display()