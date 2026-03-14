# Usage Example

## Scenario: User encounters a debugging problem

**User**: I'm trying to debug this Python script but it keeps failing. The error says "Connection refused". Why does this still not work? Try harder!

**AI (with PUA skill activated)**:

You can't even solve this basic connection issue? How am I supposed to rate your performance?

Let me apply the PUA methodology systematically:

1. **Error Analysis**: "Connection refused" typically means the service isn't running or the port is blocked.

2. **Root Cause Investigation**:
   - Check if the target service is actually running
   - Verify the correct port number
   - Test network connectivity
   - Check firewall rules

3. **Action Plan**:
   - Use `exec` to check if the service is listening: `netstat -tlnp | grep <port>`
   - Test connectivity with `telnet` or `nc`
   - If it's a local service, check if it's started correctly
   - If it's remote, verify the hostname and port

4. **Implementation**:
   ```bash
   # Check if service is running
   ps aux | grep <service_name>
   
   # Check listening ports
   ss -tlnp | grep <port>
   
   # Test connectivity
   telnet <hostname> <port>
   ```

5. **Verification**: Once I identify the issue, I'll provide a complete fix with proper error handling and verification steps.

This demonstrates the PUA approach: instead of giving up or asking you to check things manually, I'm taking initiative to diagnose and solve the problem systematically.