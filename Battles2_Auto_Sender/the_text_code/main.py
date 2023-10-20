try:
    from OpenBattles import openBattles
    from KeyboardAutoSender import keyboardAutoSend
    import Utility as util
    from mouse import wait

    if __name__ == "__main__":
        file_content = open(util.path_to_variables, "r").readlines()
        legal_keys = util.getSendHotKeys(file_content)
        
        openBattles(file_content)
        keyboardAutoSend(legal_keys)
            
except Exception as e:
    input(f"Exeption {e}\npress enter to exit program")