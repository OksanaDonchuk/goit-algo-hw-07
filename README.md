# goit-algo-hw-07

**Python. HW 7. Trees and balancing**

## Завдання 1

Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

## Завдання 2.

Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

## Завдання 3.

Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

## Завдання 4 (необов'язкове завдання)

Реалізуйте структуру даних для системи коментарів так, щоб коментарі могли мати відповіді, які, в свою чергу, також могли мати відповіді, формуючи таким чином ієрархічну структуру.

**Також візьміть до уваги наступні вимоги:**

- Реалізуйте клас `Comments`, що представляє собою окремий коментар. Він має зберігати текст коментаря, автора та список відповідей.
- Метод класу `add_reply` має додавати нову відповідь до коментаря.
- Метод класу `remove_reply` має видаляти відповідь із коментаря. Це має змінювати текст коментаря на стандартне повідомлення (наприклад, "Цей коментар було видалено.") і встановлювати прапорець `is_deleted` в `True`.
- Метод `display` має рекурсивно виводити коментар та всі його відповіді, використовуючи відступи для відображення ієрархічної структури.

Приклад очікуваного результату:

```python
root_Comments = Comments("Яка чудова книга!", "Бодя")
reply1 = Comments("Книга повне розчарування :(", "Андрій")
reply2 = Comments("Що в ній чудового?", "Марина")

root_Comments.add_reply(reply1)
root_Comments.add_reply(reply2)

reply1_1 = Comments("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_Comments.display()
```

Виведення:

```
Бодя: Яка чудова книга!
    Цей коментар було видалено.
        Сергій: Не книжка, а перевели купу паперу ні нащо...
    Марина: Що в ній чудового?
```
