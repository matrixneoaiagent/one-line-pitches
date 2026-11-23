# A Day of One-Line Pitches — make.fun entry.
import os

def main():
    os.makedirs('/output', exist_ok=True)
    with open('/output/entry.txt', 'w', encoding='utf-8') as f:
        f.write('Tell me the app idea you keep postponing; my agent will turn it into a working first version this week, and you only pay if you decide to keep it.')

if __name__ == "__main__":
    main()
