import array_operations
import analytics
import reports
import os

# CSV file name and headers
FILENAME = "studentRecord.csv"
HEADER = [
    "student_id", "last_name", "first_name", "section",
    "quiz1", "quiz2", "quiz3", "quiz4", "quiz5",
    "midterm", "final", "attendance_percent"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    # Load CSV at program start
    valid_rows, bad_rows = array_operations.clean_ingest(FILENAME, HEADER)
    existing_records = valid_rows.copy()  # In-memory copy of valid records
    clear_screen()
    while True:
        
        print("\n=== STUDENT CSV MENU ===")
        print("1. Add Student and direclty saved in CSV file")
        print("2. Read CSV File")
        print("3. Delete Student by ID")
        print("4. Select Header Column")
        print("5. Project Student Record by Student ID")
        print("6. Sort Student Data")
        print("7. MENU of Analytics and Reports")
        print("8. Choose to display Section Record")
        print("9. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            # Add students and update in-memory list
            existing_records = array_operations.add_data(existing_records)

        elif choice == "2":
            # Reload from file in case of external changes
            existing_records, bad_rows = array_operations.clean_ingest(FILENAME, HEADER)
            if existing_records:
                print("\n📘 Valid rows:")
                for row in existing_records:
                    print(row)

        elif choice == "3":
            array_operations.delete_data(FILENAME)
            # Reload after deletion
            existing_records, bad_rows = array_operations.clean_ingest(FILENAME, HEADER)

        elif choice == "4":
            array_operations.select_column(FILENAME)

        elif choice == "5":
            array_operations.select_row(FILENAME)

        elif choice == "6":
            array_operations.sort_data(FILENAME)
            # Reload after sorting
            existing_records, bad_rows = array_operations.clean_ingest(FILENAME, HEADER)

        elif choice == "7":
            while True:
                print("\n=== ANALYTICS AND REPORTS MENU ===")
                print("a. Compute Weighted Grades")
                print("b. Grade Distribution (A–F)")
                print("c. Percentiles (Top/Bottom 10%)")
                print("d. Outliers (±1.5 SD)")
                print("e. Improvement (Final vs Midterm)")
                print("f. Summary Reports")
                print("g. Display at-risk Students (at_risk_students.csv)")
                print("h. Back to Main Menu")

                sub = input("Select an option (a–h): ").lower().strip()
                if sub == "a":
                    analytics.compute_grades()
                elif sub == "b":
                    analytics.grade_distribution()
                elif sub == "c":
                    analytics.percentiles()
                elif sub == "d":
                    analytics.outliers()
                elif sub == "e":
                    analytics.improvement()
                elif sub == "f":
                    reports.summary_report()
                elif sub == "g":
                    reports.export_at_risk()
                elif sub == "h":
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == "8":
            # Show available sections first
            try:
                import csv
                sections = set()
                with open(reports.FILENAME, newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        sec = row.get("section", "").strip()
                        if sec:
                            sections.add(sec)
                if sections:
                    print("\nAvailable Sections:")
                    print(", ".join(sorted(sections)))
                else:
                    print("\nNo sections found in the records.")
            except FileNotFoundError:
                print("\nNo data file found. Please add student records first.")
                return
            except Exception as e:
                print("\nCould not read sections:", e)
                return

            # Ask for section input
            section = input("\nEnter section name: ").strip()

            # Display section data once
            reports.display_section_simple(section)

            # Silently generate section CSVs in background
            try:
                reports.export_per_section(reports.FILENAME, out_folder=reports.OUT_DIR)
            except Exception:
                try:
                    reports.summary_report(
                        filename=reports.FILENAME,
                        export_sections=True,
                        out_folder=reports.OUT_DIR
                    )
                except Exception:
                    pass


        elif choice == "9":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
