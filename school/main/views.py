from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from news.models import Polzakt
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from random import randint, sample, randrange
import time


def begin(request):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    txt, otv = [], []
    k = randint(2, 9)
    piffTr = [[3, 4, 5], [5, 12, 13], [8, 15, 17]]
    k1 = randint(0, 2)
    txt.append('1. В прямоугольном треугольнике катеты равны ' + str(piffTr[k1][0] * k) + ' и ' + str(piffTr[k1][1] * k)
               + '. Найдите гипотенузу без использования теоремы Пифагора.')
    otv.append(str(piffTr[k1][2] * k))
    k = randint(2, 9)
    piffTr.remove(piffTr[k1])
    k1 = randint(0, 1)
    txt.append('2. Найдите катет в прямоугольном треугольнике, гипотенуза в котором равна ' + str(piffTr[k1][2] * k) +
               ', а другой катет равен ' + str(piffTr[k1][0] * k) + '.')
    otv.append(str(piffTr[k1][1] * k))
    k = randint(1, 89)
    txt.append('3. В прямоугольном треугольнике один из углов равен ' + str(k) + '. Найдите второй острый угол.')
    otv.append(str(90 - k))
    a, b, c = sample(alph, 3)
    k = randint(10, 30)
    k2 = randrange(2, 5, 2)
    txt.append('4. В треугольнике ' + a + b + c + ' угол ' + c + ' равен 90°, ' + a + b + ' = ' + str(k) + ', ' + 'cos' +
               a + ' = ' + str(1 / k2) + '. Найдите ' + a + b + '.')
    otv.append(str(k / k2))
    tx = '${!$%^'.join(txt)
    ot = '${!$%^'.join(otv)
    uz = Polzakt.objects.get(idpolz=request.user.username)
    uz.pole1 = tx
    uz.pole2 = ot
    answer = request.GET
    if 'go' in answer:
        uz.save()
        request.session['ti_contr'] = time.time()
        request.session['non_zad'] = 1
        return redirect('zada4i')
    return render(request, 'main/go.html')


def zada4i(request):
    uz = Polzakt.objects.get(idpolz=request.user.username)
    text = uz.pole1.split('${!$%^')
    otvet = uz.pole2.split('${!$%^')
    text_s = []
    k = 0
    count = 0
    for i in text:
        text_s.append([str(k + 1), i])
        k += 1
    answer = request.GET
    if 'answers1' in answer:
        tm = time.time() - request.session['ti_contr']
        ot = []
        for i in answer:
            ot.append(answer[i])
        ot = ot[:-1]
        for i in range(len(otvet)):
            if otvet[i] == ot[i]:
                count += 1
        tm += 1000 * (3 - count)  # 3 - кол-во задач !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        uz = Polzakt.objects.get(idpolz=request.user.username)
        str_rec = uz.pole3.split('$')
        rec = [round(float(i)) for i in str_rec]
        razn = round((rec[request.session['non_zad'] - 1] - tm) * 10)
        absRazn = -razn
        if razn > 0:
            rec[request.session['non_zad'] - 1] = round(tm)
            rec[-1] -= razn
            str_rec = '$'.join(str(i) for i in rec)
            uz = Polzakt.objects.get(idpolz=request.user.username)
            uz.pole3 = str_rec
            uz.save()
        return render(request, 'main/pohvala.html', {'razn': razn, 'absRazn': absRazn + 1})
    return render(request, 'main/zada4i.html', {'txt': text_s})


def begin2(request):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    txt, otv = [], []
    k = randint(100, 200)
    k1 = randint(100, 200)
    txt.append('1. Диагонали четырехугольника равны ' + str(k * 13) + ' и ' + str(k1 * 13) + '.' +
               ' Найдите периметр четырехугольника,'
               'вершинами которого являются середины сторон данного четырехугольника.')
    otv.append(str(k1 + k))
    k = randint(50, 150)
    k1 = randint(50, 150)
    a, b, c = sample(alph, 3)
    txt.append('2. В четырёхугольник' + a + b + c + ' вписана окружность, ' + a + b + ' = ' + str(k) + ' и ' + 'CD = '
               + str(k1) + '.' 
               ' Найдите периметр четырёхугольника ABCD.')
    otv.append(str(2 * (k1 + k)))
    k = randint(129, 179)
    k1 = randint(50, 120)
    txt.append('3. Основания трапеции равны ' + str(k) + ' и ' + str(k1) + '.' +
               ' Найдите отрезок, соединяющий середины диагоналей трапеции.')
    otv.append(str((k - k1) / 2))
    k = randint(10, 20)
    k1 = randint(21, 35)
    txt.append('4. Основания трапеции равны ' + str(k) + ' и ' + str(k1) + '. Найдите больший из отрезков, '
               'на которые делит среднюю линию этой трапеции одна из ее диагоналей.')
    otv.append(str(k1 / 2))
    tx = '${!$%^'.join(txt)
    ot = '${!$%^'.join(otv)
    uz = Polzakt.objects.get(idpolz=request.user.username)
    uz.pole1 = tx
    uz.pole2 = ot
    answer = request.GET
    if 'go' in answer:
        uz.save()
        request.session['ti_contr'] = time.time()
        request.session['non_zad'] = 2
        return redirect('zada4i')
    return render(request, 'main/go.html')


def zada4i2(request):
    uz = Polzakt.objects.get(idpolz=request.user.username)
    text = uz.pole1.split('${!$%^')
    otvet = uz.pole2.split('${!$%^')
    return render(request, 'main/zada4i.html', {'txt': text, 'otv': otvet})


def begin3(request):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    txt, otv = [], []
    k = randint(99, 222)
    k1 = randint(2, 25)
    txt.append('1. Периметр треугольника равен ' + str(k) + ', а радиус вписанной окружности равен ' + str(k1) +
               'Найдите площадь этого треугольника.')
    otv.append(str(k / (2 * k1)))
    k = randint(79, 234)
    k1 = randint(50, 130)
    txt.append('2. В четырёхугольник, периметр которого равен ' + str(k) + ', вписана окружность, одна сторона равна' +
               str(k1) + '. Найдите длину стороны, которая лежит напротив неё.')
    otv.append(str((k / 2) - k1))
    k = randint(70, 133)
    txt.append('3. Найдите радиус окружности, вписанной в правильный треугольник, высота которого равна ' +
               str(k) + '.')
    otv.append(str(k * 3))
    a, b, c, d = sample(alph, 4)
    k = randint(15, 50)
    k1 = randint(60, 87)
    txt.append('4. Четырехугольник ' + a + b + c + d + ' вписан в окружность. Угол ' + a + b + d + ' равен ' + str(k) +
               '°, угол ' + c + a + d + ' равен ' + str(k1) + '°. Найдите угол ' + a + b + c + '.'
               ' Ответ дайте в градусах.')
    otv.append(str(k + k1))
    tx = '${!$%^'.join(txt)
    ot = '${!$%^'.join(otv)
    uz = Polzakt.objects.get(idpolz=request.user.username)
    uz.pole1 = tx
    uz.pole2 = ot
    answer = request.GET
    if 'go' in answer:
        uz.save()
        request.session['ti_contr'] = time.time()
        request.session['non_zad'] = 3
        return redirect('zada4i')
    return render(request, 'main/go.html')


def zada4i3(request):
    uz = Polzakt.objects.get(idpolz=request.user.username)
    text = uz.pole1.split('${!$%^')
    otvet = uz.pole2.split('${!$%^')
    return render(request, 'main/zada4i.html', {'txt': text, 'otv': otvet})


def begin4(request):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    piffTr = [[3, 4, 5], [5, 12, 13], [8, 15, 17]]
    txt, otv = [], []
    k = randint(99, 222)
    txt.append('1. Радиус окружности, описанной около квадрата, равен ' + str(k) + ' корней из 2.'
               ' Найдите длину стороны этого квадрата.')
    otv.append(str(k * 2))
    k = randint(79, 234)
    txt.append('2. Радиус вписанной в квадрат окружности равен ' + str(k) + ' корней из 2. Найдите радиус окружности, '
               'описанной около этого квадрата.')
    otv.append(str(k * 2))
    k = randint(90, 169)
    txt.append('3. Окружность с центром в точке O описана около равнобедренного треугольника ABC, в котором '
               'AB = BC и ∠ABC = ' + str(k) + '°. Найдите величину угла BOC. Ответ дайте в градусах.')
    otv.append(str(180 - k))
    a, b, c = sample(alph, 3)
    d = randint(0, 2)
    f, f2 = 1, 0
    k, k1 = piffTr[d][f], piffTr[d][f2]
    txt.append('4. В треугольнике ' + a + b + c + ' стороны ' +
               a + c + ' = ' + str(k) + ', ' + b + c + ' = ' + str(k1) + ', угол ' + c + ' равен 90°. '
               'Найдите радиус вписанной окружности.')
    otv.append(str((k + k1 - abs(k ** 2 + k1 ** 2)) / 2))
    tx = '${!$%^'.join(txt)
    ot = '${!$%^'.join(otv)
    uz = Polzakt.objects.get(idpolz=request.user.username)
    uz.pole1 = tx
    uz.pole2 = ot
    answer = request.GET
    if 'go' in answer:
        uz.save()
        request.session['ti_contr'] = time.time()
        request.session['non_zad'] = 3
        return redirect('zada4i')
    return render(request, 'main/go.html')


def zada4i4(request):
    uz = Polzakt.objects.get(idpolz=request.user.username)
    text = uz.pole1.split('${!$%^')
    otvet = uz.pole2.split('${!$%^')
    return render(request, 'main/zada4i.html', {'txt': text, 'otv': otvet})


def regist(request):
# return redirect('logout')
    if request.method == 'GET':
        answer = request.GET
        if 'fam' in answer and 'name' in answer and 'lg' in answer and 'email' in answer:
            f = answer.__getitem__('fam').replace(' ', '').capitalize()
            n = answer.__getitem__('name').replace(' ', '').capitalize()
            p = answer.__getitem__('email').replace(' ', '').capitalize()
            if f == '' or n == '': return redirect('regist')
            k = answer.__getitem__('kl').replace(' ', '')
            lg = answer.__getitem__('lg')
            print(lg)
            if len(f) < 2 or len(n) < 2 or len(f) > 25 or\
                    len(n) > 25 or len(k) > 25 or len(lg) > 30 or len(lg) < 3 or len(p) < 5:
                return redirect('regist')
            if User.objects.filter(username=lg).exists():
                return render(request, 'main/ujuse.html')
            else:
                Polzakt(idpolz=lg, pole1='0', famil=f, name=n, otshist=k, pole3='10000$10000$10000$10000$40000').save()
                User.objects.create_user(lg, '', '4591423', first_name=f + '$#$%' + n + '$#$%' + k).save()
                user = authenticate(request, username=lg, password='4591423')
                login(request, user)
                send_mail(
                    ' Вам письмо от администратора сайта ****, на котором Вы оставили заявку',
                    'Текст письма',
                    'u4help@u4ithelp.ru',
                    [p],
                    fail_silently=False,
                )
                return render(request, 'main/uspreg.html')
    return render(request, 'main/main_reg.html')


def index(request):
    answer = request.GET

    user_id = request.user.username
    fl0 = '0'
    if (user_id != ''):
        nm = request.user.first_name.split('$#$%')
        print('nm', nm)
        if len(nm) == 4: fl0 = '1'
        nm = nm[1]
        fl = 1
    else:
        nm = ''
        fl = 0
    # if request.method == 'GET':
    # answer = request.GET
    if 'reg' in answer: return redirect('regist')
    if 'intlg' in answer:
        lg = answer.__getitem__('lg')
        if len(lg) < 3: return redirect('home')
        if User.objects.filter(username=lg).exists() == 1:
            user = authenticate(request, username=lg, password='4591423')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'main/nezar.html')
    return render(request, 'main/index.html', {'nm': nm, 'fl': fl, 'fl0': fl0})


def table(request):
    allPolz = Polzakt.objects.all()
    mas = [[int(k) for k in i.pole3.split('$')] + [i.famil, i.name] for i in allPolz]
    mas.sort(key=lambda x: x[0])
    mas1, mas2, mas3, mas4, masSum = [], [], [], [], []
    for i in range(3):
        mas1.append([mas[i][-2], mas[i][-1], str(mas[i][0])])
    mas.sort(key=lambda x: x[1])
    for i in range(3):
        mas2.append([mas[i][-2], mas[i][-1], str(mas[i][1])])
    mas.sort(key=lambda x: x[1])
    for i in range(3):
        mas3.append([mas[i][-2], mas[i][-1], str(mas[i][2])])
    mas.sort(key=lambda x: x[1])
    for i in range(3):
        mas4.append([mas[i][-2], (mas[i][-1]), str(mas[i][3])])
    mas.sort(key=lambda x: x[1])
    for i in range(3):
        masSum.append([mas[i][-2], mas[i][-1], str(mas[i][4])])
    return render(request, 'main/table.html', {'mas1': mas1, 'mas2': mas2, 'mas3': mas3, 'mas4': mas4,
                                               'masSum': masSum})


def about(request):
    return render(request, 'main/about.html')


def zada4i_tems(request):
    return render(request, 'main/zada4i_tems.html')


#  mas1 = [i for i in
#       Polzakt.objects.filter(scores__gt='').order_by('-pole3').values_list('pole3', '')]