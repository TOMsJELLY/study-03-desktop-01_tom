import pandas as pd
import eel

@eel.expose
### デスクトップアプリ作成課題
def kimetsu_search(search_word, save_location):
    # 検索対象取得
    df = pd.read_csv("source.csv", encoding="utf_8-sig")
    # 要素を配列にして格納
    source = list(df["name"])
    
    ### 検索ツール
    word = search_word
    
    if word in source:
        return "{}が見つかりました\n".format(word)

    else:
        source.append(word)

        # CSV書き込み
        df = pd.DataFrame(source, columns=["name"])
        df.to_csv("{}.csv".format(save_location), encoding="utf_8-sig")

        return "{}は見つかりません。{}を新しく検索ソースに追加しました\n".format(word, word)

        




