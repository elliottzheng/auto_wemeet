import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys

cmd = r'"{PHTHON_PATH} {SCRIPT_PATH} meeting_code"'
cmd = cmd.replace("{PHTHON_PATH}", sys.executable)
cmd = cmd.replace("{SCRIPT_PATH}", os.path.abspath(__file__))


def read_config(encoding):
    with open("meetings.txt",encoding=encoding) as f:
        lines = f.readlines()
    return lines


def get_task_name(m_code,m_time):
    return f"AUTO_WEMEET-{m_code}-{m_time}"

def convert_time(m_time):
    return str(m_time).replace(" ","_").replace("-","_").replace(":","_")

def schedule():
    try:
        lines = read_config('utf-8')
    except:
        lines = read_config("gb2312")
    now_time = datetime.now()
    meetings = []
    for line in lines:
        m_time, m_code = line.split(",")
        for kw in ["年", "月", "日"]:
            m_time = m_time.replace(kw, ":")
        t_items = [int(i) for i in m_time.split(":")]
        m_time = datetime(*(t_items + [0]))
        if m_time < now_time:
            print("Meeting", line.strip(), "is out of date.")
            continue
        meetings.append((m_time, m_code.strip()))
    meetings = sorted(meetings, key=lambda x: x[0])
    if len(meetings) == 0:
        print("No meetings need to be scheduled, check your meetings file")
        return
    for i, (m_time, m_code) in enumerate(meetings): # 提早启动5分钟
        for m in range(5):
            n_time = m_time - relativedelta(minutes=5-m)
            if datetime.now() < n_time:
                break
        print("Schduling", m_code, "at", n_time)
        sd, st = str(n_time).split()
        
        task_name = get_task_name(m_code,convert_time(m_time))
        real_cmd = cmd.replace("meeting_code", task_name)
        os.system(
            f"SchTasks /Create /SC ONCE /TN {task_name} /TR {real_cmd} /ST {st} /SD {sd}"
        )


def launch(task_name):
    m_code = task_name.split("-")[1]
    os.system(f"start wemeet://page/inmeeting?meeting_code={m_code}")
    os.system(f"schtasks /delete /TN {task_name} /f")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        schedule()
    elif len(sys.argv) == 2:
        launch(sys.argv[1])
    else:
        raise
