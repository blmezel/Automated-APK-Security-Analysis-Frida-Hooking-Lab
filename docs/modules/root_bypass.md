# Sandbox Evasion Architecture
Intercepts file subsystem assertions (`java.io.File.exists`) targeting low-level binary validation paths (`/sbin/su`) to disguise high-privilege operations within the virtual user workspace.
