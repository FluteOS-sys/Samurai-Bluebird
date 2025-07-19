# samurai_bluebird_custos/core/main_loop.py

from samurai_bluebird_custos.core.kernel import Kernel

if __name__ == "__main__":
    print("🔵 Samurai Bluebird Custos – Resonance Genesis v0.2.1")
    print("⚡ Initializing cognitive flow engine...")
    kernel = Kernel(batch_interval=5)  # capture passive input every 5 seconds

    try:
        runtime_minutes = 1  # Run system for 1 minute for testing
        kernel.run(runtime_minutes=runtime_minutes)
    except KeyboardInterrupt:
        print("🛑 Interrupted by user. Shutting down gracefully...")
    finally:
        print("✅ Samurai Bluebird Custos – Resonance Flow ended.")
