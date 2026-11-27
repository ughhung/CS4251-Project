set pagination off
set print pretty on
set print elements 32
set may-call-functions off
info threads
thread apply all bt 20

python
import gdb


def dump_network_state():
    for name in ("sim_send_waiting_hash", "sim_recv_waiting_hash",
                 "received_msg_standby_hash"):
        try:
            value = gdb.parse_and_eval(name)
            count = value["_M_t"]["_M_impl"]["_M_node_count"]
            print(f"\n{name}: {count} keys")
            gdb.execute(f"print {name}")
        except gdb.error as error:
            print(f"{name}: {error}")


def main_frame():
    for thread in gdb.selected_inferior().threads():
        thread.switch()
        frame = gdb.newest_frame()
        while frame is not None:
            if frame.name() == "main":
                return frame
            frame = frame.older()
    return None


def dump_streams(system):
    active = gdb.default_visualizer(system["active_Streams"])
    if active is None:
        print(f"  active_Streams: {system['active_Streams']}")
        return
    # The map pretty printer emits each key followed by its value.
    children = iter(active.children())
    for (_, queue), (_, streams) in zip(children, children):
        printer = gdb.default_visualizer(streams)
        if printer is None:
            print(f"  queue {queue}: {streams}")
            continue
        for _, pointer in printer.children():
            if not int(pointer):
                continue
            stream = pointer.dereference()
            print(f"  queue {queue}, stream {stream['stream_id']}, "
                  f"{stream['current_com_type']}, state {stream['state']}, "
                  f"steps finished {stream['steps_finished']}")


def dump_rank_state():
    frame = main_frame()
    if frame is None:
        print("Main frame unavailable. Rank state could not be read.")
        return
    try:
        systems = frame.read_var("systems")["_M_impl"]
        start, end = systems["_M_start"], systems["_M_finish"]
        count = int(end - start)
        if not 0 < count <= 32:
            print(f"Unexpected rank count {count}. Rank state could not be read.")
            return
    except (gdb.error, TypeError, ValueError) as error:
        print(f"Main-frame rank state unavailable: {error}")
        return
    try:
        tracker = frame.read_var("completion_tracker").dereference()
        print(f"\nUnfinished ranks: {tracker['num_unfinished_ranks_']}/{count}")
    except (gdb.error, TypeError, ValueError) as error:
        print(f"Completion tracker unavailable: {error}")
    for rank in range(count):
        try:
            pointer = (start + rank).dereference()
            if not int(pointer):
                continue
            system = pointer.dereference()
            print(f"Rank {rank}: pending events {system['pending_events']}, "
                  f"running streams {system['total_running_streams']}, "
                  f"ready list {system['ready_list']}")
            dump_streams(system)
        except (gdb.error, TypeError, ValueError) as error:
            print(f"Rank {rank}: {error}")


dump_network_state()
dump_rank_state()
end

detach
