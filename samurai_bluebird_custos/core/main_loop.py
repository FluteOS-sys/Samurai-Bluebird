from samurai_bluebird_custos.core.kernel import Kernel

if __name__ == "__main__":
    runtime_minutes = 30  # Total run time
    interval_seconds = 300  # 5 min between snapshots

    kernel = Kernel()
    kernel.run(runtime_minutes=runtime_minutes, interval_seconds=interval_seconds)
