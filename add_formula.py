from data.formula import Formula
from data.db_session import global_init, create_session

global_init('db/formulas.sqlite')
session = create_session()

# 9 grade
formula0 = Formula()
formula0.year = 9
formula0.topic = 'Законы взаимодействия и движения тел'
formula0.formula_name = 'Формула импульса тела'
formula0.formula = 'p = mv'
formula0.explanation = 'Импульсом называют произведение массы тела на его скорость.'
formula0.explanation = 'p – импульс тела [кг·м/с], m – масса тела [кг], υ – скорость [м/с]'

formula1 = Formula()
formula1.year = 9
formula1.topic = 'Законы взаимодействия и движения тел'
formula1.formula_name = 'Формула скорости'
formula1.formula = 'v = s/t'
formula1.explanation = 'Скорость – физическая величина, равная отношению перемещения к промежутку времени, ' \
                       'за которое это перемещение произошло.'
formula1.details = 'v – скорость [м/с], s – путь [м], t – время [c]'

formula2 = Formula()
formula2.year = 9
formula2.topic = 'Законы взаимодействия и движения тел'
formula2.formula_name = 'Вычисление перемещения'
formula2.formula = 'АВ^2 = АС^2 + ВС^2'
formula2.explanation = 'Перемещение – вектор, соединяющий начальную точку движения тела с его конечной точкой.'

formula3 = Formula()
formula3.year = 9
formula3.topic = 'Законы взаимодействия и движения тел'
formula3.formula_name = 'Проекция вектора перемещения'
formula3.formula = 'Sx = x2 – x1'
formula3.details = 'x1 – начальная координата [м], x2 – конечная координата [м], Sx – перемещение [м]'

formula4 = Formula()
formula4.year = 9
formula4.topic = 'Законы взаимодействия и движения тел'
formula4.formula_name = 'Уравнение движения'
formula4.formula = 'x = x0 + vxt'
formula4.details = 'x0 – начальная координата [м], x – конечная координата [м], v – скорость [м/с], t – время [c]'

formula5 = Formula()
formula5.year = 9
formula5.topic = 'Законы взаимодействия и движения тел'
formula5.formula_name = 'Уравнение скорости'
formula5.formula = 'v = v0⃗+ at'
formula5.details = 'v – конечная скорость [м/с], v0 – начальная скорость [м/с], a – ускорение [м/с2], t – время [c]'

formula6 = Formula()
formula6.year = 9
formula6.topic = 'Законы взаимодействия и движения тел'
formula6.formula_name = 'Уравнение Галилея'
formula6.formula = 'S = v0t + at^2/2'
formula6.details = 'S – перемещение [м], v – конечная скорость [м/с], v0 – начальная скорость [м/с], ' \
                   'a – ускорение [м/с2], t – время [c]'

formula7 = Formula()
formula7.year = 9
formula7.topic = 'Законы взаимодействия и движения тел'
formula7.formula_name = 'Первый закон Ньютона'
formula7.explanation = 'Если на тело не действуют никакие тела либо их действие скомпенсировано, то это тело будет ' \
                       'находиться в состоянии покоя или двигаться равномерно и прямолинейно.'

formula8 = Formula()
formula8.year = 9
formula8.topic = 'Законы взаимодействия и движения тел'
formula8.formula_name = 'Второй закон Ньютона'
formula8.formula = 'a = F ⃗/m'
# formula8.formula = 'a = F/m'
formula8.formula = '123'
# formula8.explanation = 'Ускорение, приобретаемое телом под действием силы, прямо пропорционально величине этой силы ' \
#                        'и обратно пропорционально массе тела.'
formula8.explanation = '123'
# formula8.details = 'a – ускорение [м/с2], F – сила [Н], m – масса [кг]'
formula8.details = '123'

formula9 = Formula()
formula9.year = 9
formula9.topic = 'Законы взаимодействия и движения тел'
formula9.formula_name = 'Третий закон Ньютона'
formula9.formula = '|F1⃗ |=|F2⃗| ' \
                   'F11 ⃗ = -F2⃗'
formula9.explanation = 'Сила, с которой первое тело действует на второе, равна по модулю ' \
                       'и противоположна по направлению силе, с которой второе тело действует на первое'
formula9.details = 'F – сила, [Н]'

formula10 = Formula()
formula10.year = 9
formula10.topic = 'Законы взаимодействия и движения тел'
formula10.formula_name = 'Формула высоты, с которой падает тело'
formula10.formula = 'H=gt^2/2'
formula10.details = 'Н – высота [м], t – время [c], g ≈ 9,81 м/с2 – ускорение свободного падения'

# 10 grade

formula11 = Formula()
formula11.year = 10
formula11.topic = 'Механика'
formula11.formula_name = 'Формула скорости'
formula11.formula = 'v = s/t'
formula11.explanation = 'Скорость – физическая величина, равная отношению перемещения к промежутку времени, ' \
                        'за которое это перемещение произошло.'
formula11.details = 'v – скорость [м/с], s – путь [м], t – время [c]'

formula12 = Formula()
formula12.year = 10
formula12.topic = 'Механика'
formula12.formula_name = 'Вычисление перемещения'
formula12.formula = 'АВ^2 = АС^2 + ВС^2'
formula12.explanation = 'Перемещение – вектор, соединяющий начальную точку движения тела с его конечной точкой.'

formula13 = Formula()
formula13.year = 10
formula13.topic = 'Механика'
formula13.formula_name = 'Проекция вектора перемещения'
formula13.formula = 'Sx = x2 – x1'
formula13.details = 'x1 – начальная координата [м], x2 – конечная координата [м], Sx – перемещение [м]'

formula14 = Formula()
formula14.year = 10
formula14.topic = 'Механика'
formula14.formula_name = 'Уравнение движения'
formula14.formula = 'x = x0 + vxt'
formula14.details = 'x0 – начальная координата [м], x – конечная координата [м], v – скорость [м/с], t – время [c]'

formula15 = Formula()
formula15.year = 10
formula15.topic = 'Механика'
formula15.formula_name = 'Формула для вычисления ускорения движения тела'
formula15.formula = 'a ⃗ = v ⃗- v0⃗/t'
formula15.explanation = 'Ускорение – физическая величина, которая характеризует быстроту изменения скорости.'
formula15.details = 'a – ускорение [м/с2], v – конечная скорость [м/с], v0 – начальная скорость [м/с], t – время [c]'

formula15 = Formula()
formula15.year = 10
formula15.topic = 'Механика'
formula15.formula_name = 'Уравнение скорости'
formula15.formula = 'v ⃗ = v0 ⃗ + a ⃗t'
formula15.explanation = 'Ускорение – физическая величина, которая характеризует быстроту изменения скорости.'
formula15.details = 'v – конечная скорость [м/с], v0 – начальная скорость [м/с], a – ускорение [м/с2], t – время [c]'

formula16 = Formula()
formula16.year = 10
formula16.topic = 'Механика'
formula16.formula_name = 'Закон изменения координаты тела при прямолинейном равноускоренном движении'
formula16.formula = 'x = x0 + v0t + at^2/2'
formula16.details = 'x0 – начальная координата [м], x – конечная координата [м], v – конечная скорость [м/с], ' \
                    'v0 – начальная скорость [м/с], a – ускорение [м/с2], t – время [c]'

formula17 = Formula()
formula17.year = 10
formula17.topic = 'Механика'
formula17.formula_name = 'Первый закон Ньютона'
formula17.explanation = 'Если на тело не действуют никакие тела либо их действие скомпенсировано, то это тело будет ' \
                        'находиться в состоянии покоя или двигаться равномерно и прямолинейно.'

formula18 = Formula()
formula18.year = 10
formula18.topic = 'Механика'
formula18.formula_name = 'Второй закон Ньютона'
formula18.formula = 'a = F ⃗/m'
formula18.explanation = 'Ускорение, приобретаемое телом под действием силы, прямо пропорционально величине этой силы ' \
                        'и обратно пропорционально массе тела.'
formula18.details = 'a – ускорение [м/с2], F – сила [Н], m – масса [кг]'

formula19 = Formula()
formula19.year = 10
formula19.topic = 'Механика'
formula19.formula_name = 'Третий закон Ньютона'
formula19.formula = '|F1⃗ |=|F2⃗| ' \
                    'F11 ⃗ = -F2⃗'
formula19.explanation = 'Сила, с которой первое тело действует на второе, равна по модулю ' \
                        'и противоположна по направлению силе, с которой второе тело действует на первое'
formula19.details = 'F – сила, [Н]'

formula20 = Formula()
formula20.year = 10
formula20.topic = 'Механика'
formula20.formula_name = 'Формула высоты, с которой падает тело'
formula20.formula = 'H=gt^2/2'
formula20.details = 'Н – высота [м], t – время [c], g ≈ 9,81 м/с2 – ускорение свободного падения'

formulas = [
    formula0,
    formula1,
    formula2,
    formula3,
    formula4,
    formula5,
    formula6,
    formula7,
    formula8,
    formula9,
    formula10,
    formula11,
    formula12,
    formula13,
    formula14,
    formula15,
    formula16,
    formula17,
    formula18,
    formula19,
    formula20,
    Formula(
        year=10,
        topic='Механика',
        formula_name='Формула для вычисления высоты при движении вертикально вверх',
        formula='h=v0t - gt^2/2',
        details='h – высота [м], v0 – начальная скорость [м/с], t – время [c],'
                ' g ≈ 9,81 м/с2 – ускорение свободного падения',
    ),
    Formula(
        year=9,
        topic='Законы взаимодействия и движения тел',
        formula_name='Формула для вычисления высоты при движении вертикально вверх',
        formula='h=v0t -gt^2/2',
        details='h – высота [м], v0 – начальная скорость [м/с], t – время [c],'
                ' g ≈ 9,81 м/с2 – ускорение свободного падения',
    ),
    Formula(
        year=10,
        topic='Механика',
        formula_name='Формула для вычисления веса тела при движении вверх с ускорением',
        formula='P = m(g + a)',
        details='P – вес тела [Н], m – масса тела [кг], g ≈ 9,81 м/с2 – ускорение свободного падения, '
                'a – ускорение тела [м/с2]',
    ),
    Formula(
        year=10,
        topic='Механика',
        formula_name='Формула для вычисления веса тела при движении вниз с ускорением	',
        formula='P = m(g – a)',
        details='P – вес тела [Н], m – масса тела [кг], g ≈ 9,81 м/с2 – ускорение свободного падения, '
                'a – ускорение тела [м/с2]',
    ),
    Formula(
        year=10,
        topic='Механика',
        formula_name='Формула закона всемирного тяготения',
        formula='F = Gm1m2/r2',
        explanation='Закон всемирного тяготения: два тела притягиваются друг к другу с силой, '
                    'прямо пропорциональной произведению масс этих тел и обратно пропорциональной '
                    'квадрату расстояния между ними.',
        details='F – сила [Н], G = 6,67 · 10-11 [Н·м2/кг2] – гравитационная постоянная, m – масса тела [кг], '
                'r – расстояние между телами [м]',
    ),

    # 11 grade
    Formula(
        year=11,
        topic='Электродинамика',
        formula_name='Формула расчета силы Ампера',
        formula='FA = B I L sinα',
        explanation='Закон Ампера: сила действия однородного магнитного поля на проводник с током '
                    'прямо пропорциональна силе тока, длине проводника, модулю вектора индукции магнитного поля, '
                    'синусу угла между вектором индукции магнитного поля и проводником.',
        details='FA – сила Ампера [Н], В – магнитная индукция [Тл], I – сила тока [А], L – длина проводника [м]',
    ),
    Formula(
        year=11,
        topic='Электродинамика',
        formula_name='Формула расчета силы Ампера',
        formula='FA = B*I*L*sinα',
        explanation='Закон Ампера: сила действия однородного магнитного поля на проводник с током '
                    'прямо пропорциональна силе тока, длине проводника, модулю вектора индукции магнитного поля, '
                    'синусу угла между вектором индукции магнитного поля и проводником.',
        details='FA – сила Ампера [Н], В – магнитная индукция [Тл], I – сила тока [А], L – длина проводника [м]',
    ),

    Formula(
        year=11,
        topic='Электродинамика',
        formula_name='Формула расчета силы Лоренца',
        formula='Fл= q*B*υ*sinα',
        explanation='Сила Лоренца – сила, действующая на точечную заряженную частицу, движущуюся в магнитном поле. '
                    'Она равна произведению заряда, модуля скорости частицы, модуля вектора индукции '
                    'магнитного поля и синуса угла между вектором магнитного поля и скоростью движения частицы.',
        details='Fл – сила Лоренца [Н], q – заряд [Кл], В – магнитная индукция [Тл], '
                'υ – скорость движения заряда [м/с]',
    ),
    Formula(
        year=11,
        topic='Электродинамика',
        formula_name='Формула для вычисления магнитного потока',
        formula='Ф = B*S*cosα',
        explanation='Сила Лоренца – сила, действующая на точечную заряженную частицу, движущуюся в магнитном поле. '
                    'Она равна произведению заряда, модуля скорости частицы, модуля вектора индукции '
                    'магнитного поля и синуса угла между вектором магнитного поля и скоростью движения частицы. ',
        details='Ф – магнитный поток [Вб], В – магнитная индукция [Тл], S – площадь контура [м2] ',
    ),
    Formula(
        year=11,
        topic='Электродинамика',
        formula_name='Закон Ома для участка цепи',
        formula='I = U/R',
        explanation='Закон Ома - сила тока в участке цепи прямо пропорциональна напряжению на концах этого участка '
                    'и обратно пропорциональна его сопротивлению.',
        details='Ф – магнитный поток [Вб], В – магнитная индукция [Тл], S – площадь контура [м2]',
    ),
]

session.add_all(formulas)
session.commit()
