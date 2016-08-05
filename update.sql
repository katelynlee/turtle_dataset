UPDATE BigTable
SET Profile_ID= (SELECT Profile_ID from Profile WHERE BigTable.Age = Profile.Age AND BigTable.Sex = Profile.Sex and BigTable.Species = Profile.Species);

UPDATE BigTable
SET Cap_ID= (SELECT Cap_ID from Capture WHERE BigTable.Trap_Type = Capture.Trap_Type AND BigTable.Bait_Type = Capture.Bait_Type and BigTable.new_recap = Capture.New_Recap);

UPDATE BigTable
SET Loc_ID= (SELECT Loc_ID from Pond WHERE BigTable.Pond = Pond.Pond AND BigTable.Pond_Loc = Pond.Pond_Loc);

UPDATE BigTable
SET R_ID= (SELECT R_ID from Research WHERE BigTable.Notes = Research.Notes AND BigTable.Observer = Research.Observer);

UPDATE BigTable
SET Size_ID= (SELECT Size_ID from Size WHERE BigTable.Mass = Size.Mass AND BigTable.Carapace_L = Size.Carapace_L AND BigTable.Carapace_W = Size.Carapace_W AND BigTable.Carapace_H = Size.Carapace_H AND BigTable.Plastron_L = Size.Plastron_L);

