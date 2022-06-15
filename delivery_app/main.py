import random


tracking_no = int(random.random()*1000000000000)

    		


"""
    def tracking_no(self):
        from delivery_app.models import Tracking
        import random

        random_num =  random.randint(2345678909800, 9923456789000)

        uniqe_confirm = Tracking.objects.filter(tracking_no=random_num)

        while uniqe_confirm:
            random_num =  random.randint(2345678909800, 9923456789000)
            if not Tracking.objects.filter(tracking_no=random_num):
                break

        return random_num
    
"""