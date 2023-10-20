try:
    from OpenBattles import openBattles
    from KeyboardAutoSender import keyboardAutoSend
    import Utility as util
    from mouse import wait
    import threading
    from time import sleep
    import keyboard

    def main(stop_flag):
        file_content = open(util.path_to_variables, "r").readlines()
        legal_keys = util.getSendHotKeys(file_content)
        
        openBattles(file_content)
        while not stop_flag.is_set():
            keyboardAutoSend(legal_keys)
        
    if __name__ == "__main__":
        
        stop = threading.Event()
        
        operation_thread = threading.Thread(target=main, args=(stop,))
        operation_thread.start()
        
        sleep(5)
        while True:
            sleep(1)
            if not util.isBattlesRunning():
                break
        stop.set()
        operation_thread.join()
            
except Exception as e:
    input(f"Exeption {e}\npress enter to exit program")