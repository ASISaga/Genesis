#!/usr/bin/env python3
"""
Example: Using the Genesis Runtime API

This example demonstrates how to use the Genesis Runtime programmatically
to create, configure, and execute Genesis programs.
"""

from pathlib import Path
import sys

# Add src directory to path
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

from genesis_runtime import GenesisRuntime, RuntimeConfig, create_runtime


def example_basic_runtime():
    """Example 1: Basic runtime usage"""
    print("="*70)
    print("Example 1: Basic Runtime Usage")
    print("="*70)
    
    # Create runtime with default configuration
    runtime = create_runtime()
    
    # Load a program
    success = runtime.load_program_from_file('examples/hello-world.gen')
    if not success:
        print("Failed to load program")
        return
    
    # Execute the program
    runtime.start()
    
    # Get runtime info
    info = runtime.get_info()
    print(f"\nRuntime Info:")
    print(f"  State: {info['state']}")
    print(f"  Programs loaded: {info['programs_loaded']}")
    print(f"  Active domains: {info['metrics']['active_domains']}")


def example_custom_config():
    """Example 2: Runtime with custom configuration"""
    print("\n" + "="*70)
    print("Example 2: Custom Configuration")
    print("="*70)
    
    # Create custom configuration
    config = RuntimeConfig(
        runtime_id="demo-runtime",
        aos_mode="standalone",
        log_level="WARNING",  # Less verbose
        enable_telemetry=True,
        covenant_enforcement=True
    )
    
    # Create runtime with custom config
    runtime = GenesisRuntime(config)
    runtime.initialize()
    
    print(f"Runtime ID: {runtime.config.runtime_id}")
    print(f"AOS Mode: {runtime.config.aos_mode}")
    print(f"State: {runtime.get_state().value}")
    
    # Load and run a program
    runtime.load_program_from_file('examples/hello-world.gen', 'demo')
    runtime.start('demo')


def example_from_source():
    """Example 3: Load program from source code"""
    print("\n" + "="*70)
    print("Example 3: Loading from Source Code")
    print("="*70)
    
    # Genesis source code
    source = '''
    Domain "Direct_Example" {
        Purpose Simple {
            Objective: "Demonstrate direct source loading"
        }
        
        Pantheon "Demo_Council" {
            Avatar "Demo_Avatar" {
                Lineage: "Example_Lineage"
                Essence: "Demonstration"
            }
        }
        
        Pulse {
            Resonate {
                Threshold: Simple_Consensus(0.8)
                Synthesize {
                    "Simple demonstration"
                }
            }
            
            Manifest (on Resonance) {
                Execute: mcp.call("console.write", "Loaded from source code!")
            }
        }
    }
    '''
    
    # Create runtime and load from source
    runtime = create_runtime()
    runtime.load_program(source, program_id="from-source")
    runtime.start("from-source")


def example_metrics_monitoring():
    """Example 4: Monitoring runtime metrics"""
    print("\n" + "="*70)
    print("Example 4: Metrics Monitoring")
    print("="*70)
    
    runtime = create_runtime()
    runtime.load_program_from_file('examples/hello-world.gen')
    runtime.start()
    
    # Get detailed metrics
    metrics = runtime.get_metrics()
    print(f"\nRuntime Metrics:")
    print(f"  Uptime: {metrics.uptime_seconds:.3f} seconds")
    print(f"  Programs executed: {metrics.programs_executed}")
    print(f"  Active domains: {metrics.active_domains}")
    print(f"  Active avatars: {metrics.active_avatars}")
    
    # Get comprehensive info
    info = runtime.get_info()
    print(f"\nComprehensive Info:")
    for key, value in info.items():
        print(f"  {key}: {value}")


def example_lifecycle():
    """Example 5: Lifecycle management"""
    print("\n" + "="*70)
    print("Example 5: Lifecycle Management")
    print("="*70)
    
    # Create and initialize
    runtime = GenesisRuntime()
    print(f"Initial state: {runtime.get_state().value}")
    
    runtime.initialize()
    print(f"After init: {runtime.get_state().value}")
    
    # Load program
    runtime.load_program_from_file('examples/hello-world.gen')
    print(f"After load: {runtime.get_state().value}")
    
    # Start execution
    runtime.start()
    print(f"After execution: {runtime.get_state().value}")
    
    # Stop gracefully
    runtime.stop(graceful=True)
    print(f"After stop: {runtime.get_state().value}")


if __name__ == "__main__":
    # Run all examples
    example_basic_runtime()
    example_custom_config()
    example_from_source()
    example_metrics_monitoring()
    example_lifecycle()
    
    print("\n" + "="*70)
    print("All examples completed successfully!")
    print("="*70)
