from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # ============== Variables ==========================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        self.var_atten_subject = StringVar()
        
        
       # first header image  
        img=Image.open(r"image_collection/banner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # Background image
        bg_img3 = Image.open(r"image_collection/bg2.jpg")
        bg_img3 = bg_img3.resize((1366, 768), Image.LANCZOS)
        self.bg_photoimg3 = ImageTk.PhotoImage(bg_img3)

        bg_lbl = Label(self.root, image=self.bg_photoimg3)
        bg_lbl.place(x=0, y=130, width=1366, height=768)

        title_lbl = Label(bg_lbl, text="ATTENDANCE  MANAGEMENT  SYSTEM", font=("verdana", 25, "bold"),
                          bg="white", fg="navyblue", anchor=CENTER)
        title_lbl.place(x=0, y=0, width=1366, height=35)

        main_frame = Frame(bg_lbl, bd=2, bg="white")
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white",fg="#002B53",relief=RIDGE, text="Student Attendance Details",
                                font=("verdana", 12, "bold"))
        left_frame.place(x=10,y=10,width=660,height=480)

        # Student attendance details
        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=10, width=650, height=300)

        # Labels and Entries
        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text="Attend_ID:", font=("verdana", 11, "bold"),
                                   bg="white",fg="navyblue")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_atten_id, font=("verdana", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name
        namelabel = Label(left_inside_frame, text="Name:", bg="white",fg="navyblue", font=("verdana", 11, "bold"))
        namelabel.grid(row=1, column=0, padx=4, pady=8)

        atten_name = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_atten_name, font=("verdana", 11, "bold"))
        atten_name.grid(row=1, column=1, pady=8)

        # Roll No
        roll_label = Label(left_inside_frame, text="Roll:", bg="white", fg="navyblue",font=("verdana", 11, "bold"))
        roll_label.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_atten_roll, font=("verdana", 11, "bold"))
        atten_roll.grid(row=0, column=3, pady=8)

        # Department
        deplabel = Label(left_inside_frame, text="Department:", bg="white",fg="navyblue", font=("verdana", 11, "bold"))
        deplabel.grid(row=1, column=2, padx=10, pady=8)

        atten_dep = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_atten_dep, font=("verdana", 11, "bold"))
        atten_dep.grid(row=1, column=3, pady=8)

        # Time
        timelabel = Label(left_inside_frame, text="Time:", bg="white",fg="navyblue", font=("verdana", 11, "bold"))
        timelabel.grid(row=2, column=0, padx=10, pady=8)

        atten_time = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_atten_time, font=("verdana", 11, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        datelabel = Label(left_inside_frame, text="Date:", bg="white",fg="navyblue", font=("verdana", 11, "bold"))
        datelabel.grid(row=2, column=2, padx=4, pady=8)

        atten_date = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_atten_date, font=("verdana", 11, "bold"))
        atten_date.grid(row=2, column=3, pady=8)

        # Attendance Status
        attendancelabel = Label(left_inside_frame, text="Attend_Status:", bg="white",fg="navyblue",
                                font=("verdana", 11, "bold"))
        attendancelabel.grid(row=3, column=0, padx=10, pady=8)

        self.atten_status = ttk.Combobox(left_inside_frame, width=15, textvariable=self.var_atten_attendance, font=("verdana", 11, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)
      
        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=260, width=650, height=38)

        # Import CSV
        save_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=16, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # Export CSV
        update_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=16, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        # Update
        update_btn = Button(btn_frame, text="Update", width=16, command=self.update_data, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        # Reset
        reset_btn = Button(btn_frame, text="Reset", width=16, command=self.reset_data, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("Times New Roman", 12, "bold"))
        right_frame.place(x=680, y=10, width=660, height=500)

        # Table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=650, height=455)

        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Treeview table
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance", "subject"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        # Scrollbars for table
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Define the columns
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        

        # Show the headings
        self.AttendanceReportTable["show"] = "headings"

        # Column widths
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
       

        # Pack the table into the frame
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        # Bind the click event
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # Fetch data into table
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                               filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        if not file_name:
            messagebox.showerror("Error", "No file selected", parent=self.root)
            return
        try:
            with open(file_name) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV file: {str(e)}", parent=self.root)

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No data to export", parent=self.root)
                return
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                                     filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                                                     defaultextension=".csv", parent=self.root)
            if not file_name:
                messagebox.showerror("Error", "No file selected", parent=self.root)
                return
            with open(file_name, mode="w", newline="") as myfile:
                export_write = csv.writer(myfile, delimiter=",")
                for row in mydata:
                    export_write.writerow(row)
                messagebox.showinfo("Success", "Data exported successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Failed to export CSV: {str(es)}", parent=self.root)

    # Get cursor data
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])
      
    # Update data
    def update_data(self):
       pass
   
    # Reset data
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
