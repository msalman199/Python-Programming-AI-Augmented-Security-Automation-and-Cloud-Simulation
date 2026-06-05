import asyncio
from execution_engine import AsyncExecutionEngine

class EngineMonitor:
    """Monitor and display engine statistics."""
    
    def __init__(self, engine: AsyncExecutionEngine):
        self.engine = engine
        self.monitoring = False
    
    async def display_stats(self, interval: int = 2):
        """
        Display engine statistics periodically.
        
        Args:
            interval: Update interval in seconds
        """
        self.monitoring = True
        
        while self.monitoring:
            # TODO: Clear screen (print newlines or use os.system('clear'))
            # TODO: Get and display statistics
            # TODO: Display active workers count
            # TODO: Display queue size
            # TODO: Sleep for interval
            pass
    
    def stop(self):
        """Stop monitoring."""
        self.monitoring = False
