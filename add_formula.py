from sqlachemy.orm import select
from data.formula import Formula
from data.db_session import global_init, create_session

global_init('db/formulas.sqlite')
session = create_session()

formula1 = Formula()
formula1.grade = 9
formula1.topic = 'Законы взаимодействия и движения тел'
formula1.formula_name = 'Формула скорости'
formula1.formula = 'v = s/t'
formula1.explanation = 'Скорость – физическая величина, равная отношению перемещения к промежутку времени,' \
                       ' за которое это перемещение произошло.'
formula1.details = 'v – скорость [м/с], s – путь [м], t – время [c]'

formula2 = Formula()
formula2.grade = 9
formula2.topic = 'Законы взаимодействия и движения тел'
formula2.formula_name = 'Вычисление перемещения'
formula2.formula = 'АВ2 = АС2 + ВС2'
formula2.explanation = 'Перемещение – вектор, соединяющий начальную точку движения тела с его конечной точкой.'

formula3 = Formula()
formula3.grade = 9
formula3.topic = 'Законы взаимодействия и движения тел'
formula3.formula_name = 'Проекция вектора перемещения'
formula3.formula = 'Sx = x2 – x1'
formula3.details = 'x1 – начальная координата [м], x2 – конечная координата [м], Sx – перемещение [м]'

formula4 = Formula()
formula4.grade = 9
formula4.topic = 'Законы взаимодействия и движения тел'
formula4.formula_name = 'Уравнение движения	'
formula4.formula = 'x = x0 + vxt'
formula4.details = 'x0 – начальная координата [м], x – конечная координата [м], v – скорость [м/с], t – время [c]'

formula5 = Formula()
formula5.grade = 9
formula5.topic = 'Законы взаимодействия и движения тел'
formula5.formula_name = 'Уравнение скорости'
formula5.formula = 'v = v0⃗+ at'
formula5.details = 'v – конечная скорость [м/с], v0 – начальная скорость [м/с], a – ускорение [м/с2], t – время [c]'

formula6 = Formula()
formula6.grade = 9
formula6.topic = 'Законы взаимодействия и движения тел'
formula6.formula_name = 'Уравнение Галилея'
formula6.formula = 'S = v0t + at2/2'

formula6.details = 'S – перемещение [м], v – конечная скорость [м/с], v0 – начальная скорость, [м/с],' \
                   ' a – ускорение [м/с2],t – время, [c]'

formula7 = Formula()
formula7.grade = 9
formula7.topic = 'Законы взаимодействия и движения тел'
formula7.formula_name = 'Первый закон Ньютона'
formula7.explanation = '	Если на тело не действуют никакие тела либо их действие скомпенсировано, то это тело будет' \
                       ' находиться в состоянии покоя или двигаться равномерно и прямолинейно.'

session.add_all([
    formula1,
    formula2,
    formula3,
    formula4,
    formula5,
    formula6,
    formula7,
])

session.commit()
