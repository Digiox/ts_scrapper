import subprocess
import os
import venv
import sys
deps_file = 'requirements.txt'
def save_deps():
    # Définir le nom du fichier de sortie
    

    # Exécuter pip freeze et capturer la sortie
    pip_freeze_output = subprocess.check_output(['pip', 'freeze'])

    # Écrire la sortie dans le fichier requirements.txt
    with open(deps_file, 'wb') as file:
        file.write(pip_freeze_output)

    print(f'Le fichier {deps_file} a été créé avec succès.')


def install_deps():


    # Vérifier si l'environnement virtuel est activé
    if 'VIRTUAL_ENV' in os.environ:
        print(f"L'environnement virtuel est activé : {os.environ['VIRTUAL_ENV']}")
    else:
        print("Aucun environnement virtuel n'est activé.")
        exit()
        # print("Souhaitez vous créer un environnement venv ?")
        # selection = input("Oui ou non")

        # if (selection.lower() == "oui"):
        #     # Définir le chemin où l'environnement virtuel sera créé
        #     env_dir = 'venv'

        #     # Créer l'environnement virtuel
        #     builder = venv.EnvBuilder(clear=True, with_pip=True)
        #     builder.create(env_dir)

        #     print(f"L'environnement virtuel a été créé dans le dossier : {os.path.abspath(env_dir)}")
        #     print("Souhaitez vous activer l'environnement ?")

        #     selection = input("Oui ou non")
        #     if (selection.lower() == "oui"):
        #         # Demander à l'utilisateur de spécifier son système d'exploitation
        #         system = input("Entrez votre système d'exploitation (windows/unix): ").lower()

        #         # Définir le chemin du script d'activation en fonction du système d'exploitation
        #         if system == 'windows':
        #             activate_script = f'{env_dir}\\Scripts\\activate.bat'
        #         elif system == 'unix':
        #             activate_script = f'{env_dir}/bin/activate'
        #         else:
        #             print("Système d'exploitation non reconnu.")
        #             sys.exit(1)

        #         # Commande pour activer l'environnement virtuel
        #         subprocess.run([sys.executable, "-m", "venv", activate_script])
        #     else:
        #         exit()


    print(f'Checking if {deps_file} is present')

    if (os.path.isfile(deps_file)):
        print(f'{deps_file} file is present, stating to install dependencies')
    else: 
        print(f'{deps_file} is not present in this project, exiting...')
        exit()
    # Fonction pour installer les dépendance
    try:
        # Exécuter la commande pip install
        subprocess.check_call(['pip', 'install', '-r', deps_file])
        print(f"Les dépendances du fichier '{deps_file}' ont été installées avec succès.")
    except subprocess.CalledProcessError as e:
        # Afficher un message d'erreur en cas d'échec
        print(f"Erreur lors de l'installation des dépendances : {e}")

def main():
    entry = input("Select an action (fetch or save): ")
    if (entry == "save"):
        save_deps()
    elif (entry == "fetch"):
        install_deps()
    else: 
        print("Action not recognized")

main()