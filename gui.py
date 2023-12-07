from tkinter import *
import gpa


class Gui:
    def __init__(self, window):
        self.window = window

        # Radio buttons
        self.frame_student = Frame(self.window)
        self.label_operation = Label(self.frame_student, text='Pick a number of classes')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_one = Radiobutton(self.frame_student, text='1', variable=self.radio_1, value=1,
                                     command=self.classes)
        self.radio_two = Radiobutton(self.frame_student, text='2', variable=self.radio_1, value=2,
                                     command=self.classes)
        self.radio_three = Radiobutton(self.frame_student, text='3', variable=self.radio_1, value=3,
                                       command=self.classes)
        self.radio_four = Radiobutton(self.frame_student, text='4', variable=self.radio_1, value=4,
                                      command=self.classes)
        self.radio_five = Radiobutton(self.frame_student, text='5', variable=self.radio_1, value=5,
                                      command=self.classes)
        self.label_operation.pack(side='left', padx=5)
        self.radio_one.pack(side='left')
        self.radio_two.pack(side='left')
        self.radio_three.pack(side='left')
        self.radio_four.pack(side='left')
        self.radio_five.pack(side='left')
        self.frame_student.pack(anchor='w', pady=10)

        # First number
        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first)
        self.entry_first = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=20, side='left')
        self.entry_first.pack(padx=20, side='left')
        self.frame_first.pack(anchor='w', pady=10)
        self.entry_first.pack_forget()

        # Second number
        self.frame_second = Frame(self.window)
        self.label_second = Label(self.frame_second)
        self.entry_second = Entry(self.frame_second, width=40)
        self.label_second.pack(padx=20, side='left')
        self.entry_second.pack(padx=20, side='left')
        self.frame_second.pack(anchor='w', pady=10)
        self.entry_second.pack_forget()

        # Third number
        self.frame_third = Frame(self.window)
        self.label_third = Label(self.frame_third)
        self.entry_third = Entry(self.frame_third, width=40)
        self.label_third.pack(padx=20, side='left')
        self.entry_third.pack(padx=20, side='left')
        self.frame_third.pack(anchor='w', pady=10)
        self.entry_third.pack_forget()

        # Fourth number
        self.frame_fourth = Frame(self.window)
        self.label_fourth = Label(self.frame_fourth)
        self.entry_fourth = Entry(self.frame_fourth, width=40)
        self.label_fourth.pack(padx=20, side='left')
        self.entry_fourth.pack(padx=20, side='left')
        self.frame_fourth.pack(anchor='w', pady=10)
        self.entry_fourth.pack_forget()

        # Fifth number
        self.frame_fifth = Frame(self.window)
        self.label_fifth = Label(self.frame_fifth)
        self.entry_fifth = Entry(self.frame_fifth, width=40)
        self.label_fifth.pack(padx=20, side='left')
        self.entry_fifth.pack(padx=20, side='left')
        self.frame_fifth.pack(anchor='w', pady=10)
        self.entry_fifth.pack_forget()

        # Results label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Compute button
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='Compute GPA', command=self.compute)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def classes(self):
        self.entry_first.delete(0, END)
        self.entry_second.delete(0, END)
        self.entry_third.delete(0, END)
        self.entry_fourth.delete(0, END)
        self.entry_fifth.delete(0, END)
        self.label_result.config(text='')
        self.entry_first.pack()

        class_number = self.radio_1.get()

        if class_number == 1:
            self.label_first.config(text='Enter your grade:')
            self.label_second.config(text='')
            self.label_third.config(text='')
            self.label_fourth.config(text='')
            self.label_fifth.config(text='')
            self.entry_second.pack_forget()
            self.entry_third.pack_forget()
            self.entry_fourth.pack_forget()
            self.entry_fifth.pack_forget()

        elif class_number == 2:
            self.label_first.config(text='Enter your first grade:')
            self.label_second.config(text='Enter your second grade:')
            self.label_third.config(text='')
            self.label_fourth.config(text='')
            self.label_fifth.config(text='')
            self.entry_second.pack()
            self.entry_third.pack_forget()
            self.entry_fourth.pack_forget()
            self.entry_fifth.pack_forget()

        elif class_number == 3:
            self.label_first.config(text='Enter your first grade:')
            self.label_second.config(text='Enter your second grade:')
            self.label_third.config(text='Enter your third grade:')
            self.label_fourth.config(text='')
            self.label_fifth.config(text='')
            self.entry_second.pack()
            self.entry_third.pack()
            self.entry_fourth.pack_forget()
            self.entry_fifth.pack_forget()

        elif class_number == 4:
            self.label_first.config(text='Enter your first grade:')
            self.label_second.config(text='Enter your second grade:')
            self.label_third.config(text='Enter your third grade:')
            self.label_fourth.config(text='Enter your fourth grade:')
            self.label_fifth.config(text='')
            self.entry_second.pack()
            self.entry_third.pack()
            self.entry_fourth.pack()
            self.entry_fifth.pack_forget()

        elif class_number == 5:
            self.label_first.config(text='Enter your first grade:')
            self.label_second.config(text='Enter your second grade:')
            self.label_third.config(text='Enter your third grade:')
            self.label_fourth.config(text='Enter your fourth grade:')
            self.label_fifth.config(text='Enter your fifth grade:')
            self.entry_second.pack()
            self.entry_third.pack()
            self.entry_fourth.pack()
            self.entry_fifth.pack()

    def compute(self):
        try:
            y = self.radio_1.get()
            class_number = y
            nums = [self.entry_first.get(), self.entry_second.get(), self.entry_third.get(),
                    self.entry_fourth.get(), self.entry_fifth.get()]
            x = len(nums) - 1

            while y != len(nums):
                nums.pop(x)
                x -= 1

            if class_number == 1:
                self.label_result.config(text=f'Your GPA is {gpa.math(nums)}')

            elif class_number == 2:
                self.label_result.config(text=f'Your GPA is {gpa.math(nums)}')

            elif class_number == 3:
                self.label_result.config(text=f'Your GPA is {gpa.math(nums)}')

            elif class_number == 4:
                self.label_result.config(text=f'Your GPA is {gpa.math(nums)}')
            elif class_number == 5:
                self.label_result.config(text=f'Your GPA is {gpa.math(nums)}')

            else:
                self.label_result.config(text='No operation selected')

        except ValueError:
            self.label_result.config(text='Enter numeric values')

        except TypeError:
            self.label_result.config(text='Values must be positive')
