# c++ way, backward, O(n)
class solution():
    def replace_blank(self, str):
        re_str = str.replace(' ', '%20')
        return re_str


if __name__ == '__main__':
    sol = solution()
    str = 'we are happy.'
    print(sol.replace_blank(str))
