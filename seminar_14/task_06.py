"""
На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.
"""

from seminar_13.task_05 import User, Project

from pytest import fixture, main


@fixture
def get_file(tmp_path):
    f_name = tmp_path / 'task_06.json'
    with open(f_name, 'w+', encoding='utf-8') as f:
        f.write("""
        {
  "1": {
    "1": "Алексей",
    "11": "Алексей"
  },
  "2": {
    "2": "Евгений"
  },
  "3": {
    "3": "Василиса"
  },
  "4": {
    "4": "Анастасия"
  },
  "5": {
    "5": "Владимир"
  },
  "6": {
    "6": "Шамиль"
  },
  "7": {
    "7": "Станислас"
  }
}""")
        f.seek(0)
    return f_name


def test_read_users(get_file):
    """Все элементы в списке являются экземплярами класса User"""
    assert all(isinstance(user, User) for user in Project.read_users(get_file))


def test_print_users(capfd, get_file):
    """Проверка корректного вывода пользователей"""
    print(*Project.read_users(get_file), sep="\n")
    out, err = capfd.readouterr()
    assert out == ('User 1 (Алексей) has access level 1\n'
                   'User 11 (Алексей) has access level 1\n'
                   'User 2 (Евгений) has access level 2\n'
                   'User 3 (Василиса) has access level 3\n'
                   'User 4 (Анастасия) has access level 4\n'
                   'User 5 (Владимир) has access level 5\n'
                   'User 6 (Шамиль) has access level 6\n'
                   'User 7 (Станислас) has access level 7\n')


def test_creation_user():
    """Проверка создания пользователя"""
    user = User(1, 1, "Алексей")
    assert user.access_level == 1
    assert user.user_id == 1
    assert user.name == "Алексей"
    assert str(user) == "User 1 (Алексей) has access level 1"


def test_user_set_params():
    """Проверка установки параметров пользователя"""
    user = User(1, 1, "Алексей")
    user.user_id = 2
    user.name = "Евгений"
    user.access_level = 2
    assert user.access_level == 2
    assert user.user_id == 2
    assert user.name == "Евгений"
    assert str(user) == "User 2 (Евгений) has access level 2"


def test_users_eq():
    """Проверка равенства объектов класса User"""
    user_1 = User(1, 1, "Алексей")
    user_2 = User(1, 1, "Алексей")
    assert user_1 == user_2


def test_project_get_user_by_id(get_file):
    p = Project(get_file)
    assert p.get_user_by_id("1") == User(1, "1", "Алексей")


def test_project_get_user(get_file):
    p = Project(get_file)
    assert p.get_user("1", "Алексей") == User(1, "1", "Алексей")


if __name__ == '__main__':
    main(['-v'])
