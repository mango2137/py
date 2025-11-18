import os

FILE_NAME = "tasks.txt"

def wczytaj_z_pliku():
    tasks = []
    if not os.path.exists(FILE_NAME):
        return tasks

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split("|")
            if len(parts) == 3:
                title, priority, done = parts
                tasks.append([title, priority, done == "1"])
    return tasks


def zapisz_do_pliku(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for t in tasks:
            line = f"{t[0]}|{t[1]}|{'1' if t[2] else '0'}\n"
            f.write(line)
    print("💾 Zapisano do pliku.")


def dodaj_zadanie(lista):
    title = input("Podaj tytuł zadania: ")
    priority = input("Podaj priorytet (wysoki/średni/niski): ").lower()
    lista.append([title, priority, False])
    print("Dodano zadanie.")


def pokaz_zadania(lista):
    if not lista:
        print("Brak zadań.")
        return

    print("\n--- LISTA ZADAŃ ---")
    for i, (title, priority, done) in enumerate(lista):
        status = "[✔]" if done else "[ ]"
        print(f"{i}. {status} {title} (priorytet: {priority})")
    print("-------------------\n")


def zrob_zadanie(lista):
    pokaz_zadania(lista)
    try:
        idx = int(input("Podaj numer zadania do oznaczenia jako wykonane: "))
        lista[idx][2] = True
        print("Zadanie oznaczone jako wykonane.")
    except:
        print("❗ Niepoprawny numer.")


def usun_zadanie(lista):
    pokaz_zadania(lista)
    try:
        idx = int(input("Podaj numer zadania do usunięcia: "))
        lista.pop(idx)
        print("Usunięto zadanie.")
    except:
        print("❗ Niepoprawny numer.")


def main():
    tasks = wczytaj_z_pliku()
    print("📌 Wczytano istniejące zadania.")

    while True:
        cmd = input("Co chcesz zrobić? [dodaj/lista/zrob/usun/save/load/exit]: ").lower()

        if cmd == "dodaj":
            dodaj_zadanie(tasks)

        elif cmd == "lista":
            pokaz_zadania(tasks)

        elif cmd == "zrob":
            zrob_zadanie(tasks)

        elif cmd == "usun":
            usun_zadanie(tasks)

        elif cmd == "save":
            zapisz_do_pliku(tasks)

        elif cmd == "load":
            tasks = wczytaj_z_pliku()
            print("📂 Wczytano dane z pliku.")

        elif cmd == "exit":
            print("Do zobaczenia!")
            break

        else:
            print("❗ Nieznana komenda.")

main()
