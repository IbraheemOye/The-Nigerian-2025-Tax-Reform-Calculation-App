--Create a database
CREATE DATABASE Nigeria_Tax_Reform

--Create a table called Tax Calculations
CREATE TABLE New_Tax_Calculations (
id INT PRIMARY KEY,
states VARCHAR (20),
gross_income VARCHAR (20),
pension_contribution VARCHAR (20),
consolidated_relief_allowance VARCHAR (20),
taxable_income VARCHAR (20),
income_tax VARCHAR (20),
total_deductions VARCHAR (20),
net_income VARCHAR (20)
);
  
  INSERT INTO New_Tax_Calculations (id, states, gross_income, pension_contribution, consolidated_relief_allowance, taxable_income, income_tax, total_deductions, net_income)
VALUES (001, 'Lagos', 500000, 40000, 100000, 360000, 65633, 105633, 394367),
(002, 'Kano', 300000, 24000, 60000, 216000, 34860, 58860, 241140),
(003, 'Abuja', 400000, 32000, 80000, 288000, 49980, 81980, 318020),
(004, 'Imo', 200000, 16000, 40000, 144000, 19860, 35860, 164140),
(005, 'Lagos', 100000, 8000, 20833, 71166, 7175, 15175, 84825);

