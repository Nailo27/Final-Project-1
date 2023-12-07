import csv


def math(x):
    """
    Obtains the list from the gui and names it nums
    total_gpa is set to 0.00
    The for loop turns the values from nums to floats
    The try/except ensures that it is greater than 0 and a number.
        Once that's true, then it adds a gpa based on what your grade was.
    Finally, the total_gpa is divided by the length of nums and is returned.
    :param x: The list of grades
    """
    nums = x
    total_gpa = 0.00
    length = len(nums)

    for i in range(len(nums)):
        nums[i] = float(nums[i])

        try:
            """
            Determines whether the value is over or under a certain amount.
            Once it finds that value, it adds a certain value to total_gpa
            """
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

        except isinstance(nums[i], str):
            raise ValueError

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
