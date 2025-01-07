from time import sleep

class User:
    def __init__ (self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode=False, time_now=0):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False

class UrTube:
    def __init__(self, *attrib):
        self.current_user = None
        self.users = []
        self.videos = []

    def add (self, *data): # РАБОТАЕТ #
        for (i) in range (len (data)) :
            if len(self.videos) == 0:
                self.videos.append(data[i])
            else:
                for j in range (len (self.videos)):
                    tmp_videos = (str (self.videos [j].title))
                    if data [i] .title in tmp_videos :
                        break
                    else :
                        self.videos.append ( data [i] )
                        break
                continue

    def get_videos(self, temp_serch): # РАБОТАЕТ #
        fin_serch = []
        temp_serch = temp_serch.lower()
        for i in range(len(self.videos)):
            temp_video = (str(self.videos[i].title)).lower()
            if temp_serch in temp_video:
                fin_serch.append(str(self.videos[i].title))
            else:
                continue
        return fin_serch

    def watch_video(self, data):
        for i in range(len(self.videos)):
            temp_video = str(self.videos[i].title)
            if data == temp_video :
                if self.current_user is None :
                    print("Войдите в аккаунт, чтобы смотреть видео")
                else :
                    for j in range(len(self.users)):
                        if self.current_user in str(self.users[j].nickname):
                            if int(str(self.users[j].age)) < 18:
                                print ('Вам нет 18 лет, пожалуйста покиньте страницу')
                                break
                            else :
                                temp_duration = int(str(self.videos[j].duration))
                                for k in range (temp_duration):
                                    print (self.videos[j].time_now, end=' ')
                                    self.videos[j].time_now = self.videos[j].time_now + 1
                                    sleep(1)
                                self.videos[j].time_now = 0
                                print ("Конец видео")


    # def __repr__(self):
    #     return

    def log_in (self, nickname, password):
        password = hash (password)
        for i in range (len (self.users)):
            if nickname in self.users[i].nickname:
                if password == self.users[i].password:
                    self.current_user = nickname
                else :
                    continue
            else :
                continue

    def register (self, nickname, password, age):
        if len (self.users) == 0 :
            self.users.append(User(nickname, hash (password), age))
        else :
            for i in range(len (self.users)):
                if nickname in self.users[i].nickname:
                    print (f"Пользователь {nickname} уже существует")
                    break
                else :
                    self.users.append(User(nickname, hash(password), age))
        ur.log_in(nickname, password)

    def log_out (self):
        self.current_user = None

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

ur.add(v1, v2)

# # Проверка поиска

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# # Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# # Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')