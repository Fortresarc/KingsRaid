import Settings

try :
    Settings.WriteDefaultSettingsFile ()
    Settings.ReadFromFile ()
except SystemExit:
	pass