from pathlib import Path

def get_cats_info(file_path: Path) -> list:
    cat_lst = []
    try:
        with open(file_path, "r", encoding="utf-8") as cats:
            for cat in cats:
                res = cat.strip().split(",")
                cat_info_dict = {
                    "id": res[0],
                    "name": res[1],
                    "age": res[2]
                }
                cat_lst.append(cat_info_dict)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
      
    return cat_lst

print(get_cats_info(Path("cats/cats_file.txt")))
