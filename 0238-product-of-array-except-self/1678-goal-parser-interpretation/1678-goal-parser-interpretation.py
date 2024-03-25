class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace('(','.(')
        command = command.replace(')', ').')

        command_list = command.split('.')
        for i in range(len(command_list)):
            if command_list[i] == '()':
                command_list[i] = 'o'
            elif command_list[i] == '(al)':
                command_list[i] = 'al'

        return ''.join(command_list)
