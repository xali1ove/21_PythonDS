from analytics import Research
from config import  *

def main(): # пока хз удалить или нет
    try:
        res = Research(file_path)
        data = res.file_reader()

        observations_num = len(data)
        analist = Research.Analytics(data)
        count = analist.counts()
        fract = analist.fractions(count)

        ran = analist.predict_random(num_of_steps)
        head_r, tail_r = analist.calc_predict_random(ran)
        file = template.format(
            observations_num,
            count[0],
            count[1],
            fract[0],
            fract[1],
            num_of_steps,
            head_r,
            tail_r
        )
        analist.save_file(file, out_file, '.txt')

    except Exception as err:
        print(type(err).__name__, err, sep=': ')

if __name__ == "__main__":
    main()