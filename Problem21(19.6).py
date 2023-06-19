def custom_sort(item):
    # تحديد الكلمات التي يجب تجاهلها
    ignore_words = ["An", "A", "The"]
    
    # تقسيم العبارة إلى كلمات فردية
    words = item.split()
    
    # إزالة الكلمات التي يجب تجاهلها من القائمة
    filtered_words = [word for word in words if word not in ignore_words]
    
    # الانضمام لإعادة بناء العبارة المصححة
    corrected_item = ' '.join(filtered_words)
    
    return corrected_item

# المصفوفة الأصلية
input_list = ["The real one", "An Arrangment", "A Royalty", "Establishment", "The Avengers", "An occupation"]

# تطبيق الفرز بناءً على الدالة المخصصة
sorted_list = sorted(input_list, key=custom_sort)

# طباعة المصفوفة المرتبة
print(sorted_list)
