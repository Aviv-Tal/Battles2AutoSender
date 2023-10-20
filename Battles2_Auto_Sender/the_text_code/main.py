try:
    from OpenBattles import openBattles
    from KeyboardAutoSender import keyboardAutoSend
    import Utility as util
    from mouse import wait
    from threading import Thread
    from time import sleep
    
    def main_program() -> None:
        file_content = open(util.path_to_variables, "r").readlines()
        legal_keys = util.getSendHotKeys(file_content)
        
        openBattles(file_content)
        keyboardAutoSend(legal_keys)
    
    def auto_shutdown() -> None:
        sleep(10)
        while util.isBattlesRunning():
            pass
        exit()

    if __name__ == "__main__":
        program_thread = Thread(target=main_program)
        auto_shutdown_thread = Thread(target=auto_shutdown)
        
        program_thread.start()
        auto_shutdown_thread.start()
        
            
except Exception as e:
    print(f"Exeption {e}\ndeal with it")