def add_even():
    # طلب إدخال رقم من المستخدم
    number = int(input('Enter an even number: '))
    
    # التحقق من أن الرقم يقع في النطاق من 1 إلى 106
    if number < 1 or number > 106:
        print('Please enter a number between 1 and 106.')
        return None  # إنهاء الدالة
    
    # التحقق مما إذا كان الرقم المدخل زوجيًا
    if number % 2 != 0:
        print('The number entered is not even.')
        return None  # إنهاء الدالة
    
    # معالجة الحالات الخاصة
    if number == 1:
        print('There is no even number less than one.')
        return 0  # إعادة مجموع الأرقام الزوجية (0 لأنه لا يوجد)
    elif number == 2:
        print('There is only one even number: 2.')
        return 2  # إعادة مجموع الأرقام الزوجية (فقط 2)
    
    # حساب مجموع الأرقام الزوجية
    total_sum = 0
    for i in range(2, number + 1, 2):  # تمر فقط على الأرقام الزوجية
        total_sum += i
    
    # إرجاع الناتج
    return total_sum

# استدعاء الدالة وطباعة الناتج
result = add_even()
if result is not None:
    print(f'The sum of even numbers is: {result}')
                 
    