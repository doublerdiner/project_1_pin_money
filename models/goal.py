import datetime

class Goal:
    def __init__(self, name, savings_target, savings_time_frame, saved_so_far=0, id=None):
        self.name = name
        self.savings_target = savings_target
        self.savings_time_frame = savings_time_frame
        self.saved_so_far = saved_so_far
        self.id = id
        self.time_left = []
        
    def time_remaining(self):
        today = datetime.datetime.today()
        time = str(self.savings_time_frame)
        new = datetime.datetime.strptime(time, "%Y-%m-%d")

        years = new.year - today.year
        months = new.month - today.month
        days = new.day - today.day

        self.time_left = [days, months, years]
        return self.time_left
    # Calculates the time remaining from today until the savings due date.
    
    def goal_comment(self):
        if self.time_left[2] > 0:
            return f"You have {self.time_left[2]} years to meet your goal!"
        elif self.time_left[1] > 0:
            return f"You have {self.time_left[1]} months to meet your goal!"
        elif self.time_left[0] > 0:
            return f"You have {self.time_left[0]} days to meet your goal!"
        else:
            return f"Your goal due date has passed. Please update your goal"
        
    def goal_calculation(self):
        months = (self.time_left[2]*12) + self.time_left[1]
        to_be_saved = self.savings_target
        if months >= 0:
            to_be_saved = (self.savings_target - self.saved_so_far) / months
            to_be_saved = round(to_be_saved, 2)
        return to_be_saved
