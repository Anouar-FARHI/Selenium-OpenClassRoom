import os
import datetime

class Logger:
    def __init__(self):
        self.date_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.log_files = {}
        self.base_log_path = "/app/logs"  # Chemin de base pour les logs à l'intérieur du conteneur
    
    def get_log_file(self, log_type):
        if log_type not in self.log_files:
            log_directory = os.path.join(self.base_log_path, log_type)
            os.makedirs(log_directory, exist_ok=True)
            log_file_path = os.path.join(log_directory, f"{log_type}-{self.date_str}.log")
            self.log_files[log_type] = log_file_path
        
        # Assurez-vous que le chemin pour le fichier log général est toujours là
        log_general_path = os.path.join(self.base_log_path, "log", f"log-{self.date_str}.log")
        self.log_files["log"] = log_general_path
        
        return self.log_files[log_type]

    def log(self, log_type, message):
        log_file_path = self.get_log_file(log_type)
        log_general_path = self.log_files["log"]  # Accéder au chemin du fichier log général
        
        # Écriture dans le fichier de type spécifique
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"{datetime.datetime.now().isoformat()} - {message}\n")
        
        # Écriture dans le fichier log général
        if log_file_path != log_general_path:  # Éviter d'écrire deux fois la même chose si c'est déjà le fichier log
            with open(log_general_path, 'a') as general_log:
                general_log.write(f"{datetime.datetime.now().isoformat()} - {message}\n")
