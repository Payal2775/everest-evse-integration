import asyncio
import websockets
from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call_result
from ocpp.v16.enums import RegistrationStatus

class ChargePoint(cp):

    @on('BootNotification')
    async def on_boot_notification(self, charge_point_model, charge_point_vendor, **kwargs):
        print("Charge point connected!")

        return call_result.BootNotificationPayload(
            current_time="2026-01-01T00:00:00Z",
            interval=10,
            status=RegistrationStatus.accepted
        )

    @on('Heartbeat')
    async def on_heartbeat(self):
        return call_result.HeartbeatPayload(
            current_time="2026-01-01T00:00:00Z"
        )

    @on('StatusNotification')
    async def on_status_notification(self, **kwargs):
        print("Status update received")
        return call_result.StatusNotificationPayload()

    @on('SecurityEventNotification')
    async def on_security_event(self, **kwargs):
        print("Security event received")
        return call_result.SecurityEventNotificationPayload()


async def on_connect(websocket):
    charge_point_id = "CP_1"
    print("Client connected!")

    cp_instance = ChargePoint(charge_point_id, websocket)
    await cp_instance.start()


async def main():
    server = await websockets.serve(on_connect, "0.0.0.0", 9000)
    print("OCPP Server running on ws://localhost:9000")
    await server.wait_closed()


asyncio.run(main())
