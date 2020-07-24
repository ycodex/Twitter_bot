from apscheduler.schedulers.blocking import BlockingScheduler
import main
sched = BlockingScheduler()

@sched.scheduled_job('cron',hour=12)
def timed_job():
    main.main()


sched.start()
