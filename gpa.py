import csv


def math(x):
    """
    Obtains the list from the gui and names it nums
    total_gpa is set to 0.00
    The first for loop ensures that the list of grades, nums, are all floats
    The second for loop checks what the grade would be then adds that score to the gpa
    Finally, the total_gpa is divided by the length of nums and is returned.
    :param x: The list of grades
    """
    nums = x
    total_gpa = 0.00
    length = len(nums)

    for i in range(len(nums)):
        try:
            """
            Determines whether the value is over or under a certain amount.
            Once it finds that value, it adds a certain value to total_gpa
            """
            nums[i] = float(nums[i])
            print(nums[i])
            if nums[i] >= 90:
                if 93 <= nums[i]:
                    total_gpa += 4.0
                elif 90 <= nums[i] < 93:
                    total_gpa += 3.7

            elif 90 > nums[i] >= 80:
                if 87 <= nums[i] < 90:
                    total_gpa += 3.3
                elif 83 <= nums[i] < 87:
                    total_gpa += 3.0
                elif 80 <= nums[i] < 83:
                    total_gpa += 2.7

            elif 80 > nums[i] >= 70:
                if 80 > nums[i] >= 77:
                    total_gpa += 2.3
                elif 77 > nums[i] >= 73:
                    total_gpa += 2.0
                elif 73 > nums[i] >= 70:
                    total_gpa += 1.7

            elif 70 < nums[i] >= 65:
                if 67 <= nums[i] < 70:
                    total_gpa += 1.3
                elif 65 <= nums[i] < 67:
                    total_gpa += 1.0

            elif 0 < nums[i] < 65:
                total_gpa += 0

            elif 0 > nums[i]:
                raise TypeError

        except 0 > nums[i]:
            raise TypeError

    total_gpa = total_gpa / (len(nums))
    calculated_gpa = round(total_gpa, 3)
    writing_grades(calculated_gpa, length)
    return calculated_gpa


def writing_grades(gpa, class_number):
    """
    Obtains the calculated gpa and amount of classes
    Puts the amount of classes and gpa into a csv file names collected_gpa.csv
    :param gpa: calculated gpa
    :param class_number: number of classes
    :return:
    """

    title = ['# of Classes', 'GPA']
    inputs = [class_number, gpa]

    filename = 'collected_gpa.csv'

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(title)
        csvwriter.writerow(inputs)
