import random

from datacenter.models import Schoolkid, Mark, Lesson
from datacenter.models import Chastisement, Commendation


def find_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__iexact__contains=name)
        return schoolkid
    except ObjectDoesNotExist:
        print("Поиск дал результат больше чем 1.")
    except MultipleObjectsReturned:
        print("Ученик с таким именем не найден.")
    return None


def fix_marks(name):
    schoolkid = find_schoolkid(name)
    if not schoolkid:
        print("Ученик с таким именем не найден.")
        return
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    if not bad_marks:
        print('У этого ученика нет плохих оценок.')
    else:
        bad_marks.update(points=5)
        print('Все плохие оценки ученика изменены на 5.')


def remove_chastisements(name):
    schoolkid = find_schoolkid(name)
    if not schoolkid:
        print("Ученик с таким именем не найден.")
        return
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    if not chastisements:
        print('У этого ученика нет наказаний.')
    else:
        chastisements.delete()
        print('Все наказания ученика удалены.')


def create_commendation(name, subject):
    schoolkid = find_schoolkid(name)
    if not schoolkid:
        print("Ученик с таким именем не найден.")
        return
    lesson = random.choice(Lesson.objects.filter(subject__title=subject))
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]
    Commendation.objects.create(
        text = random.choice(commendations),
        created = lesson.date,
        schoolkid = schoolkid,
        subject = lesson.subject,
        teacher = lesson.teacher
    )
    print(f'Похвала добавлена ученику для урока {lesson.subject.title}')
