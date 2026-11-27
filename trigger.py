"""create or replace trigger t1 instead of insert or update on  v1
for each row 

declare 
   new_expnese number;
begin 
  new_expense := :new.expenswe
  bdms_output.put_line('new income eequal'||:new.expense);
end;
/
set serveroutput on;"""