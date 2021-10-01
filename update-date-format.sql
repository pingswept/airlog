UPDATE readings
SET date = substr(date, 7, 4) || '-' ||
             substr(date, 1, 2) || '-' ||
             substr(date, 4, 2) || substr(date, 12, 9) WHERE rowid < 131134;
--Ugggggh.
